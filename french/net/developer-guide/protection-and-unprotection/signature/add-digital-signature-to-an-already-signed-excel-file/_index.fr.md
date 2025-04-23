---
title: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/net/add-digital-signature-to-an-already-signed-excel-file/
description: Cet article décrit comment ajouter une signature numérique à un fichier Excel déjà signé à l aide de codes C# avec Aspose.Cells for .Net.
keywords: Ajouter une signature numérique à un fichier Excel déjà signé, comment ajouter une signature numérique à un document Excel déjà signé.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la méthode [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé, si le document original est généré par Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier tel quel après son chargement et sa réenregistrement, ce qui rendra la signature originale invalide.

{{% /alert %}}

## **Comment ajouter une signature numérique à un fichier Excel déjà signé**

Le code d'exemple suivant a démontré comment utiliser la méthode [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) pour ajouter une signature numérique à un fichier Excel déjà signé. Veuillez vérifier le [fichier Excel d'exemple](50528280.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. Veuillez vérifier le [fichier Excel de sortie](50528281.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé [AsposeDemo.pfx](50528279.pfx) dans ce code qui a un mot de passe **aspose**. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple après son exécution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
{{< app/cells/assistant language="csharp" >}}
