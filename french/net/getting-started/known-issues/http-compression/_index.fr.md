---
title: Compression HTTP
type: docs
weight: 10
url: /fr/net/http-compression/
---
## **Problème de compression HTTP**
Certains utilisateurs signalent que s'ils configurent la compression HTTP dans IIS, ils trouvent des erreurs lors de l'envoi des fichiers générés aux navigateurs clients.
### **Explication**
 Nous utilisons**"Content-disposition", "inline; filename=test.xls"** header pour forcer le navigateur à ouvrir le fichier et**"Content-disposition", "pièce jointe ; filename=test.xls"** en-tête pour forcer le navigateur à ouvrir le**Enregistrer sous** boîte de dialogue et utilisez Microsoft Excel pour ouvrir le fichier. Cependant, certaines exceptions existent.
### **Exceptions**
Vous pouvez utiliser le code suivant pour vérifier qu'il ne s'agit PAS d'un bogue de Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Solutions**
Vous pouvez utiliser l'une des solutions de contournement suivantes pour résoudre ce problème :

- Déplacez les fichiers ASP.NET spécifiés (qui contiennent le code appelant Aspose.Cells) vers un autre dossier, qui n'est pas compressé.
- Désactivez la compression HTTP pour le contenu dynamique.
- Enregistrez le fichier généré sur votre serveur et fournissez un lien à vos utilisateurs.

 Si vous souhaitez utiliser la compression HTTP, veuillez toujours utiliser*OuvrirDansExcel* au lieu de*Ouvrir dans le navigateur* option lorsque vous savez que vous avez activé la compression IIS.
