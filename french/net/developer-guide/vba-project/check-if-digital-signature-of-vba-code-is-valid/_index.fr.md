---
title: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide à l'aide du[**Workbook.VbaProject.IsValidSignedWorkbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) propriété. Il reviendra**vrai** si la signature est valide sinon elle reviendra**faux**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifiez si la signature numérique du code VBA est valide dans C#**

 Le code suivant illustre l'utilisation de cette propriété à l'aide de la propriété[exemple de fichier excel](5115030.xlsm)que vous pouvez télécharger à partir du lien fourni. Le même fichier Excel a une signature valide, mais lorsque nous modifions son code VBA et enregistrons le classeur, puis revérifions, nous constatons que sa signature est devenue invalide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
