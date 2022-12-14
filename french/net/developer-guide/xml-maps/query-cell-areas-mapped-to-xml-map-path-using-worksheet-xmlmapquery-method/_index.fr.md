---
title: Requête Cell Zones mappées au chemin de carte XML à l'aide de la méthode Worksheet.XmlMapQuery
type: docs
weight: 60
url: /fr/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Scénarios d'utilisation possibles**

Vous pouvez interroger les zones de cellules mappées au chemin de mappage XML avec Aspose.Cells à l'aide de la[**Feuille de calcul.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)méthode. Si le chemin existe, il renverra la liste des zones de cellules liées à ce chemin dans la carte XML. Le premier paramètre de la[**Feuille de calcul.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)La méthode spécifie le chemin d'accès de l'élément XML et le deuxième paramètre spécifie une carte XML que vous souhaitez interroger.

## **Requête Cell Zones mappées au chemin de carte XML à l'aide de la méthode Worksheet.XmlMapQuery**

 La capture d'écran suivante montre le Microsoft Excel affichant la carte XML à l'intérieur du[exemple de fichier Excel](55541790.xlsx) utilisé dans le code. Le code interroge le mappage XML deux fois et imprime la liste des zones de cellule renvoyée par le[**Feuille de calcul.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)méthode sur la console comme indiqué ci-dessous.

![tâche : image_autre_texte](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Sortie console**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Obtenir le chemin XML de l'objet/table de liste**

Les données XML peuvent être importées dans des feuilles de calcul. Parfois, un chemin XML est requis à partir des ListObjects de la feuille de calcul. Cette fonctionnalité est disponible dans Excel en utilisant une expression telle que Sheet1.ListObjects(1).XmlMap.DataBinding. La même fonctionnalité est disponible au Aspose.Cells en appelant[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). L'exemple suivant illustre cette fonctionnalité. Le fichier de modèle et d'autres fichiers source peuvent être téléchargés à partir des liens suivants :

1. [Données XML.xlsx](72417285.xlsx)
1. [Liste des pays.xml](72417287.xml)
1. [Liste des aliments.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
