from fastapi import FastAPI
import pandas as pd

app = FastAPI()

pats = pd.read_csv('signatures.tsv', sep='\t')
pats.rename(columns={'Unnamed: 0': 'patient_identifier'}, inplace=True)
patients = pats.set_index('patient_identifier')


@app.get('/', status_code=200)
def get_all_signatures_for_all():
    return [(i, dict(patients.loc[i])) for i in patients.index]


@app.get('/{name}', status_code=200)
def get_all_signatures_for_one(name: str):
    return {name: patients.loc[name]}


@app.get('/{name}/{signature_name}', status_code=200)
def get_signature(name: str, signature_name: str):
    return {
        f"Для пациента {name} показателем {signature_name} является: {dict(patients.loc[name])[signature_name]}"}
