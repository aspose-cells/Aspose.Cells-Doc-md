---
title: Lecture du fichier CSV avec plusieurs encodages via Golang en C++
linktitle: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/go-cpp/reading-csv-file-with-multiple-encodings/
description: Découvrez comment lire des fichiers CSV avec plusieurs encodages en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple, PDF ou XLSX.

{{% /alert %}}

Aspose.Cells fournit la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/), que vous devez définir à **true** pour charger correctement votre fichier CSV avec plusieurs encodages.

La capture d'écran suivante montre un fichier CSV d'exemple contenant deux lignes. La première ligne est en encodage **ANSI** et la seconde en **Unicode**.

|**Fichier d'entrée**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus sans définir la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) à **true**. Comme vous pouvez le voir, le texte Unicode n'a pas été converti correctement.

|**Fichier de sortie 1: aucune adaptation pour plusieurs encodages**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus après avoir réglé la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) à **true**. Comme vous pouvez le voir, le texte Unicode est désormais converti correctement.

|**Fichier de sortie 2: IsMultiEncoded est défini sur true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ci-dessous se trouve le code d'exemple qui convertit le fichier CSV ci-dessus en format XLSX correctement.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## Articles Connexes

- [Ouverture des fichiers CSV](/cells/fr/cpp/opening-files-with-different-formats/#opening-csv-files)
