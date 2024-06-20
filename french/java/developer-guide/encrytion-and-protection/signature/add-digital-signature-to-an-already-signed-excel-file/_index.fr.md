---
title: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la méthode [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé, si le document original est généré par Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier tel quel après son chargement et sa réenregistrement, ce qui rendra la signature originale invalide.

{{% /alert %}}

## **Ajouter une signature numérique à un fichier Excel déjà signé**

Le code d'exemple suivant explique comment utiliser la méthode [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) pour ajouter une signature numérique à un fichier Excel déjà signé. Veuillez vérifier le [fichier Excel exemple](50528287.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. Veuillez vérifier le [fichier Excel de sortie](50528288.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé [AsposeTest.pfx](50528289.pfx) dans ce code, qui a un mot de passe *aspose*. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel de démonstration après son exécution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
