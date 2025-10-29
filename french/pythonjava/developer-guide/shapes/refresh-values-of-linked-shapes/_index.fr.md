---
title: Actualiser les valeurs des formes liées
type: docs
weight: 3200
url: /fr/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, le changement de la valeur de la cellule liée change également la valeur de la forme liée. Cela fonctionne également bien avec Aspose.Cells si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous voulez enregistrer votre classeur au format PDF ou HTML, alors vous devrez appeler la méthode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) pour rafraîchir la valeur de la forme liée.

{{% /alert %}}

## Exemple

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous. Il contient une image liée liée aux cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells et ensuite appeler la méthode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) pour actualiser la valeur de l'image et l'enregistrer au format PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Vous pouvez télécharger le [fichier Excel source](sampleRefreshValueOfLinkedShapes.xlsx) et le [PDF de sortie](95584292.pdf) à partir des liens donnés.

### Code C# pour rafraîchir les valeurs des formes liées

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
