---
title: Problème d Exception de sécurité
type: docs
weight: 30
url: /fr/net/security-exception-issue/
---

## **Problème d'exception de sécurité**
Certains utilisateurs peuvent recevoir une erreur "Exception de sécurité" lorsqu'ils tentent d'utiliser Aspose.Cells. Ce problème se produit généralement dans une application Web.
### **Explication**
Aspose.Cells doit appeler certaines API **Win32 GDI** pour fournir certaines fonctionnalités importantes. Si le serveur web a un niveau de confiance strict, cette exception de sécurité peut être levée.
### **Solution**
Veuillez essayer de créer un nouvel ensemble de permissions pour donner la permission de sécurité à Aspose.Cells.dll avec "Autoriser les appels aux assemblies non managées" activé.
