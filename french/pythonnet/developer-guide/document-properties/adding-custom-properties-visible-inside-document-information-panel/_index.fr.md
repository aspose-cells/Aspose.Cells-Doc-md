---
title: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 300
url: /fr/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Ajout de propriétés personnalisées visibles dans le volet Informations sur le document**

Aspose.Cells pour Python via .NET peut être utilisé pour ajouter des propriétés personnalisées à l’intérieur de l’objet classeur qui sont visibles dans le panneau d’informations du document. Vous pouvez ouvrir ce panneau dans Microsoft Excel via Fichier > Infos > Propriétés > Afficher le panneau du document.

Veuillez utiliser la méthode [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) pour ajouter une propriété personnalisée qui sera visible dans le volet Informations sur le document

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a aucun type et la deuxième propriété a un type DateTime. Une fois que vous ouvrirez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le volet Informations sur le document.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Article connexe**

{{% alert color="primary" %}}

- [Utiliser des parties XML personnalisées dans Aspose.Cells](/cells/fr/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
