---
title: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells fournit le[**Classeur.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter que lors de l'ajout d'une signature numérique à un document Excel déjà signé, si le document original est un document généré Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier après l'avoir chargé et réenregistré, cela rendra la signature originale invalide.

{{% /alert %}}

## **Ajouter une signature numérique à un fichier Excel déjà signé**

L'exemple de code suivant explique comment utiliser[**Classeur.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) méthode pour ajouter une signature numérique à un fichier Excel déjà signé. S'il vous plaît, vérifiez le[exemple de fichier Excel](50528287.xlsx)utilisé dans ce code. Ce fichier est déjà signé numériquement. S'il vous plaît, vérifiez le[fichier Excel de sortie](50528288.xlsx)généré par le code. Nous avons utilisé le certificat de démonstration nommé[AsposeTest.pfx](50528289.pfx)dans ce code qui a un mot de passe*poser*La capture d'écran montre l'effet de l'exemple de code sur l'exemple de fichier Excel après l'exécution.

![tâche : image_autre_texte](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
