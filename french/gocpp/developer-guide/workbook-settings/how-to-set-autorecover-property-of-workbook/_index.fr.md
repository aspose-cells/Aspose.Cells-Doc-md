---
title: Comment définir la propriété AutoRecover du classeur avec Golang via C++
linktitle: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Apprenez comment activer ou désactiver la propriété AutoRecover d un classeur en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover d'un classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** dans un classeur, Microsoft Excel désactive AutoRecover (Autosave) sur ce fichier Excel.

Aspose.Cells fournit la propriété [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) pour activer ou désactiver cette option.

{{% /alert %}}

Le code suivant explique comment utiliser la propriété [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) du classeur. Le code lit d'abord la valeur par défaut de cette propriété, qui est **true**, puis la définit à **false** et enregistre le classeur. Ensuite, il relit le classeur et lit la valeur de cette propriété, qui est **false** à ce moment.

## Code C++ pour définir la propriété AutoRecover du classeur

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Sortie**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
