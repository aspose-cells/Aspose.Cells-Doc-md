---
title: Problème d'exception de sécurité
type: docs
weight: 30
url: /fr/net/security-exception-issue/
---
## **Problème d'exception de sécurité**
Certains utilisateurs peuvent recevoir une erreur "Security Exception" en essayant d'utiliser Aspose.Cells. Ce problème se produit généralement dans une application Web.
### **Explication**
 Aspose.Cells doit appeler certains**API Win32 GDI** pour fournir quelques fonctionnalités importantes. Si le serveur Web a un niveau de confiance strict, cette exception de sécurité peut être levée.
### **La solution**
Veuillez essayer de créer un nouvel ensemble d'autorisations pour accorder l'autorisation de sécurité Aspose.Cells.dll avec "Autoriser les appels aux assemblys non gérés" activé.
