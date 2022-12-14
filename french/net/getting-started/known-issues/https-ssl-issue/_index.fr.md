---
title: Problème SSL HTTPS
type: docs
weight: 20
url: /fr/net/https-ssl-issue/
---
## **Problème HTTPS/SSL**
Certains utilisateurs ont signalé qu'ils avaient des problèmes pour télécharger les fichiers Excel générés avec Aspose.Cells. Lorsque la boîte de dialogue d'enregistrement s'ouvre, le nom du fichier contient le nom de la page aspx au lieu du fichier Excel et le type de fichier est vide.
### **Explication**
Nous avons modifié les en-têtes de réponse HTTP pour résoudre le problème de compression HTTP. Cela peut causer des problèmes lors de l'envoi de fichiers au navigateur client via HTTPS/SSL.
### **La solution**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
