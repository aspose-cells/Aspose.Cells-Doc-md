---
title: Problème de document non enregistré
type: docs
weight: 40
url: /fr/net/document-not-saved-issue/
---
## **Publier**
J'ai un problème étrange avec une feuille de calcul que j'ai créée avec votre contrôle. Il s'ouvre et s'édite très bien dans Excel, mais lorsque j'essaie d'effectuer un Enregistrer ou Enregistrer sous, j'obtiens une boîte de dialogue "Document non enregistré".
### **Résumé de la question**
 C'est un bogue d'Excel :

"Document non enregistré" Enregistrement du fichier créé à partir d'un modèle

ID de l'article : 121942

Dernière révision : 15 août 2005

Révision : 1.3

Cet article a été précédemment publié sous Q121942
### **Symptôme**
 Lorsque vous essayez d'enregistrer un classeur, vous pouvez recevoir le message d'erreur suivant :**"Document non enregistré"**
### **causes**
Ce problème peut se produire lorsque les conditions suivantes sont remplies :

- Le classeur a été créé à partir d'un modèle contenant un objet incorporé.
- Vous avez inséré une feuille de calcul dans votre classeur à partir d'un modèle.
- Le modèle contient un objet incorporé.
### **La solution**
Pour enregistrer votre travail, vous devez d'abord supprimer les objets incorporés dans votre classeur.
