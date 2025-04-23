---
title: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 200
url: /fr/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells pour Python via .NET fournit la propriété [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe de l'objet OLE intégré. Les identifiants de classes d'objets OLE sont en réalité des GUID, c'est-à-dire des identifiants universellement uniques. Un GUID fait toujours 16 octets de long, donc les identifiants de classe le sont aussi. Ils se trouvent souvent dans le Registre Windows et fournissent des informations à l'application hôte sur comment ouvrir l'objet OLE intégré contenant diverses ressources intégrées à l'intérieur de l'application cliente.

## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**
La capture d'écran suivante montre l'identifiant de classe de l'objet Ole, c'est-à-dire le GUID qui a été lu à partir du [fichier excel exemple](5115190.xls) contenant l'objet OLE PowerPoint incorporé.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Code d'exemple**
Veuillez consulter le code d'exemple suivant exécuté avec [fichier excel exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet Ole, c'est-à-dire le GUID. Le GUID affiché est exactement le même que celui montré dans la capture d'écran.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **Sortie console**
Ceci est la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
