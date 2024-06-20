---
title: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 200
url: /fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe de l'objet OLE incorporé. Les identifiants de classe des objets Ole sont en fait des GUID, c'est-à-dire des identifiants globalement uniques. Le GUID est toujours long de 16 octets, donc les identifiants de classe sont également longs de 16 octets. Ils sont souvent trouvés à l'intérieur du Registre Windows et fournissent des informations à l'application hôte sur la manière d'ouvrir l'objet OLE incorporé contenant diverses ressources incorporées dans l'application cliente.
## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**
La capture d'écran suivante montre l'identifiant de classe de l'objet Ole, c'est-à-dire le GUID qui a été lu à partir du [fichier excel exemple](5115190.xls) contenant l'objet OLE PowerPoint incorporé.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Code d'exemple**
Veuillez consulter le code d'exemple suivant exécuté avec [fichier excel exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet Ole, c'est-à-dire le GUID. Le GUID affiché est exactement le même que celui montré dans la capture d'écran.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Sortie console**
Ceci est la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
