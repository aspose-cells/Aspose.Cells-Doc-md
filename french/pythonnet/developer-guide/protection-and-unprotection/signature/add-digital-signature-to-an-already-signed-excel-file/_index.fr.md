---
title: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: Cet article décrit comment ajouter une signature numérique à un fichier Excel déjà signé en utilisant des codes C# avec Aspose.Cells pour Python via .NET.
keywords: Ajouter une signature numérique à un fichier Excel déjà signé, comment ajouter une signature numérique à un document Excel déjà signé.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells pour Python via .NET fournit la méthode [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé, si le document original est généré par Aspose.Cells pour Python via .NET, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par ex. Microsoft Excel), Aspose.Cells pour Python via .NET ne peut pas garder le fichier identique après le chargement et la sauvegarde, cela rendra la signature originale invalide.

{{% /alert %}}

## **Comment ajouter une signature numérique à un fichier Excel déjà signé**

Le code d'exemple suivant a démontré comment utiliser la méthode [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) pour ajouter une signature numérique à un fichier Excel déjà signé. Veuillez vérifier le [fichier Excel d'exemple](50528280.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. Veuillez vérifier le [fichier Excel de sortie](50528281.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé [AsposeDemo.pfx](50528279.pfx) dans ce code qui a un mot de passe **aspose**. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple après son exécution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

