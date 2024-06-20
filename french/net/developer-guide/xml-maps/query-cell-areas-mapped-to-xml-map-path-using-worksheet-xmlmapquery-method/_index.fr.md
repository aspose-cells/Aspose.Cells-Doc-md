---
title: Interroger les zones de cellules mappées au chemin de la carte XML en utilisant la méthode Worksheet.XmlMapQuery
type: docs
weight: 60
url: /fr/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Scénarios d'utilisation possibles**

Vous pouvez interroger les zones de cellules mappées au chemin de la carte XML avec Aspose.Cells en utilisant la méthode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery). Si le chemin existe, il renverra la liste des zones de cellules liées à ce chemin à l'intérieur de la carte XML. Le premier paramètre de la méthode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) spécifie le chemin de l'élément XML et le deuxième paramètre spécifie une carte XML que vous souhaitez interroger.

## **Interroger les zones de cellules mappées sur le chemin de carte XML en utilisant la méthode XmlMapQuery de la feuille de calcul**

La capture d'écran suivante montre Microsoft Excel affichant la carte XML à l'intérieur du [fichier Excel d'exemple](55541790.xlsx) utilisé dans le code. Le code interroge la carte XML deux fois et imprime la liste des zones de cellules retournées par la méthode [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) sur la console comme indiqué ci-dessous.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Sortie console**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Obtenir le chemin XML à partir de l'objet Liste / Tableau**

Les données XML peuvent être importées dans les feuilles de calcul. Parfois, le chemin XML est requis à partir des ListObjects de la feuille de calcul. Cette fonctionnalité est disponible dans Excel en utilisant une expression telle que Sheet1.ListObjects(1).XmlMap.DataBinding. La même fonctionnalité est disponible dans Aspose.Cells en appelant [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). L'exemple suivant démontre cette fonctionnalité. Le fichier modèle et les autres fichiers sources peuvent être téléchargés à partir des liens suivants :

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
