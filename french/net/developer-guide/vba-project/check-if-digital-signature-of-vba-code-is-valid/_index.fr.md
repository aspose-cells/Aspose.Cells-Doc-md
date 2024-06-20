---
title: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned). Elle retournera **true** si la signature est valide, sinon elle retournera **false**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide en C#**

Le code suivant démontre l'utilisation de cette propriété en utilisant le [fichier Excel d'exemple](5115030.xlsm), que vous pouvez télécharger à partir du lien fourni. Le même fichier Excel a une signature valide mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis vérifions à nouveau, nous constatons que sa signature est devenue invalide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
