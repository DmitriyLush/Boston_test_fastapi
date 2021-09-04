from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

pats = pd.read_csv('signatures.tsv', sep='\t')
pats.rename(columns={'Unnamed: 0': 'patient_identifier'}, inplace=True)
patients = pats.set_index('patient_identifier')


@app.get('/', status_code=200)
def get_all_signatures_for_all() -> dict:
    all_patients_info = {}
    for i in patients.index:
        all_patients_info[i] = dict(patients.loc[i])
    return all_patients_info


@app.get('/{name}', status_code=200)
def get_all_signatures_for_one(name: str) -> dict:
    if name not in patients.index.tolist():
        raise HTTPException(status_code=404, detail='Name not found')
    return {'Patient': name,
            'Patient signatures': patients.loc[name]}


@app.get('/{name}/{signature_name}', status_code=200)
def get_signature(name: str, signature_name: str) -> dict:
    if name not in patients.index.tolist() or signature_name not in dict(patients.loc[name]):
        raise HTTPException(status_code=404, detail='Name or signature not found')
    return {'Patient': name,
            'Patient signature': dict(patients.loc[name])[signature_name]}
