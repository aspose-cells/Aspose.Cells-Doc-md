---
title: Compression HTTP
type: docs
weight: 10
url: /fr/net/http-compression/
---

## **Problème de compression HTTP**
Certains utilisateurs signalent que s'ils configurent la compression HTTP dans IIS, ils rencontrent des erreurs lors de l'envoi de fichiers générés aux navigateurs clients.
### **Explication**
Nous utilisons l'en-tête **"Content-disposition", "inline; filename=test.xls"** pour forcer le navigateur à ouvrir le fichier et **"Content-disposition", "attachment; filename=test.xls"** pour forcer le navigateur à ouvrir la boîte de dialogue **Enregistrer sous** et utiliser Microsoft Excel pour ouvrir le fichier. Cependant, il existe quelques exceptions.
### **Exceptions**
Vous pouvez utiliser le code suivant pour vérifier qu'il ne s'agit PAS d'un bogue d'Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Solutions**
Vous pouvez utiliser l'un des contournements suivants pour résoudre ce problème :

- Déplacez les fichiers ASP.NET spécifiés (qui contiennent du code appelant Aspose.Cells) dans un autre dossier, qui n'est pas compressé.
- Désactivez la compression HTTP pour le contenu dynamique.
- Enregistrez le fichier généré sur votre serveur et fournissez un lien à vos utilisateurs.

Si vous souhaitez utiliser la compression HTTP, veuillez toujours utiliser l'option *OpenInExcel* au lieu de l'option *OpenInBrowser* lorsque vous savez que vous avez activé la compression IIS.
