---
title: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed). Elle renverra **true** si la signature est valide, sinon elle renverra **false**. La signature numérique du code VBA devient invalide si vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide en Python**

Le code suivant démontre l'utilisation de cette propriété en utilisant le [fichier Excel d'exemple](5115030.xlsm), que vous pouvez télécharger à partir du lien fourni. Le même fichier Excel a une signature valide mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis vérifions à nouveau, nous constatons que sa signature est devenue invalide.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
