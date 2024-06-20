---
title: Comment détecter un format de fichier et vérifier si le fichier est chiffré
type: docs
weight: 2700
url: /fr/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension du fichier ne garantit pas que le contenu du fichier est approprié. Le fichier pourrait être chiffré (un fichier protégé par mot de passe) afin qu'il ne puisse pas être lu directement, ou nous ne devrions pas le lire. Aspose.Cells fournit la méthode statique [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) et quelques API pertinentes que vous pouvez utiliser pour traiter des documents.

{{% /alert %}}

L'exemple de code suivant illustre comment détecter un format de fichier (en utilisant le chemin du fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est chiffré.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
