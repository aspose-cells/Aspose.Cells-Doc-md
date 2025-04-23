---
title: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells vous permet de charger de tels fichiers CSV et de les convertir en d'autres formats, par exemple, PDF ou XLSX.

{{% /alert %}}

Aspose.Cells fournit la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), que vous devez définir sur **true** pour charger correctement votre fichier CSV avec plusieurs encodages.

La capture d'écran suivante montre un exemple de fichier CSV contenant deux lignes. La première ligne est en encodage **ANSI** et la deuxième ligne est en encodage **Unicode**

|**Fichier d'entrée**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du fichier CSV ci-dessus sans définir la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) sur **true**. Comme vous pouvez le constater, le texte Unicode n'a pas été correctement converti.

|**Fichier de sortie 1: aucune adaptation pour plusieurs encodages**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La capture d'écran suivante montre le fichier XSLX converti à partir du fichier CSV ci-dessus après avoir défini la propriété [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) sur **true**. Comme vous pouvez le constater, le texte Unicode est maintenant correctement converti.

|**Fichier de sortie 2: IsMultiEncoded est défini sur true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ci-dessous se trouve le code d'exemple qui convertit le fichier CSV ci-dessus en format XLSX correctement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Articles Connexes

- [Ouverture des fichiers CSV](/cells/fr/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
