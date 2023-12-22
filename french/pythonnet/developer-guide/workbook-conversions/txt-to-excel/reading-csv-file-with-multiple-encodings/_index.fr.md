---
title: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/python-net/reading-csv-file-with-multiple-encodings/
description: Lecture du fichier CSV avec plusieurs encodages en utilisant Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells vous permet de charger de tels fichiers CSV et de les convertir dans d'autres formats, par exemple PDF ou XLSX.

{{% /alert %}}

 Aspose.Cells fournit le[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) propriété, que vous devez définir sur**vrai** pour charger correctement votre fichier CSV avec plusieurs encodages.

 La capture d'écran suivante montre un exemple de fichier CSV contenant deux lignes. La première ligne est dans**ANSI** encodage et la deuxième ligne est en**Unicode** codage

|**Fichier d'entrée**|
| :- |
|![tâche : image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du fichier CSV ci-dessus sans définir le[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)propriété à *true**. Comme vous pouvez le constater, le texte Unicode n'a pas été converti correctement.

|**Fichier de sortie 1 : aucun aménagement n'est effectué pour l'encodage multiple**|
| :- |
|![tâche : image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 La capture d'écran suivante montre le fichier XSLX converti à partir du fichier CSV ci-dessus après avoir défini le[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)propriété à *true**. Comme vous pouvez le constater, le texte Unicode est désormais correctement converti.

|**Fichier de sortie 2 : IsMultiEncoded est défini sur true**|
| :- |
|![tâche : image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Vous trouverez ci-dessous l'exemple de code qui convertit correctement le fichier CSV ci-dessus au format XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
