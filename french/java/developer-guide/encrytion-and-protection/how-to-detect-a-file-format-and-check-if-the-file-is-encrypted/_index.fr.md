---
title: Comment détecter un format de fichier et vérifier si le fichier est crypté
type: docs
weight: 2000
url: /fr/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension du fichier ne garantit pas que le contenu du fichier est approprié. Le fichier peut être crypté (un fichier protégé par mot de passe) afin qu'il ne puisse pas être lu directement, ou nous ne devrions pas le lire. Aspose.Cells fournit le[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)méthode statique et certaines API pertinentes que vous pouvez utiliser pour traiter les documents.

{{% /alert %}}

## **Code Java pour détecter le format de fichier et vérifier si le fichier est crypté**

L'exemple de code suivant montre comment détecter un format de fichier (à l'aide du chemin d'accès au fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est crypté.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
