---
title: Problème de document non enregistré
type: docs
weight: 40
url: /fr/net/document-not-saved-issue/
---

## **Problème**
J'ai un problème étrange avec une feuille de calcul que j'ai créée avec votre contrôle. Elle s'ouvre et se modifie correctement dans Excel, mais lorsque j'essaie d'enregistrer ou de sauvegarder sous, je reçois une boîte de dialogue "Document non enregistré".
### **Résumé du problème**
Il s'agit d'un bogue d'Excel : 

"Document non enregistré" Enregistrement du fichier créé à partir du modèle

ID de l'article : 121942

Dernière révision : 15 août 2005

Révision : 1.3

Cet article a été précédemment publié sous Q121942
### **Symptôme**
Lorsque vous tentez d'enregistrer un classeur, vous pouvez recevoir le message d'erreur suivant : **"Document non enregistré"**
### **Causes**
Ce problème peut survenir lorsque les conditions suivantes sont remplies :

- Le classeur a été créé à partir d'un modèle qui contenait un objet intégré.
- Vous avez inséré une feuille de calcul dans votre classeur à partir d'un modèle.
- Le modèle contient un objet intégré.
### **Solution**
Pour enregistrer votre travail, vous devez d'abord supprimer les objets intégrés de votre classeur.
