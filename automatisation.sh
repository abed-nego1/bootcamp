#!/bin/bash/
etudiants = []
def ajouter_etudiants(nom, note):
        etudiants.append({"nom": nom, "note": note})
        print(f"Etudiant {nom} ajouté avec la note {note}.")

def calcul_moyenne():
        if not etuidants:
        print ("Aucun étudiants enregistré.")
        return 0
     total= sul(e['note'] for e in entudiants)
        moyenne= total/len(etudiants)
        print(f"Moyenne de la classe :{moyenne:.2f}")
        return moyenne

def afficher_notes():
        if not etudiants:
        print ("Aucun étudiants.")
        return 0
     for i in etudiants: 
        print(f"-{e['nom']}: {e['note']}/20")


