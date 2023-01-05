---
title: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells fournit le[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)méthode que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter que lors de l'ajout d'une signature numérique à un document Excel déjà signé, si le document original est un document généré Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier après l'avoir chargé et réenregistré, cela rendra la signature originale invalide.

{{% /alert %}}

## **Ajouter une signature numérique à un fichier Excel déjà signé**

L'exemple de code suivant montre comment utiliser[**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) méthode pour ajouter une signature numérique à un fichier Excel déjà signé. S'il vous plaît, vérifiez le[exemple de fichier Excel](50528280.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. S'il vous plaît, vérifiez le[fichier Excel de sortie](50528281.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé[AsposeDemo.pfx](50528279.pfx) dans ce code qui a un mot de passe**poser**La capture d'écran montre l'effet de l'exemple de code sur l'exemple de fichier Excel après l'exécution.

![tâche : image_autre_texte](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
