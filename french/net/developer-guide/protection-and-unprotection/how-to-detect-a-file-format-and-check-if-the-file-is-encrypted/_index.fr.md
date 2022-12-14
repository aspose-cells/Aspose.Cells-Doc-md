---
title: Comment détecter un format de fichier et vérifier si le fichier est crypté
type: docs
weight: 2700
url: /fr/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension du fichier ne garantit pas que le contenu du fichier est approprié. Le fichier peut être crypté (un fichier protégé par mot de passe) afin qu'il ne puisse pas être lu directement, ou nous ne devrions pas le lire. Aspose.Cells fournit le[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) méthode statique et certaines API pertinentes que vous pouvez utiliser pour traiter les documents.

{{% /alert %}}

L'exemple de code suivant montre comment détecter un format de fichier (à l'aide du chemin d'accès au fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est crypté.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
