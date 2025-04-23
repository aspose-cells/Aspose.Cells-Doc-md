---
title: Comment détecter un format de fichier et vérifier si le fichier est chiffré
type: docs
weight: 2700
url: /fr/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension du fichier ne garantit pas que le contenu du fichier est approprié. Le fichier pourrait être chiffré (protégé par mot de passe) et ne peut pas être lu directement, ou nous ne devons pas le lire. Aspose.Cells pour Python via .NET fournit la méthode [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) statique et quelques API pertinentes que vous pouvez utiliser pour traiter les documents.

{{% /alert %}}

L'exemple de code suivant illustre comment détecter un format de fichier (en utilisant le chemin du fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est chiffré.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

