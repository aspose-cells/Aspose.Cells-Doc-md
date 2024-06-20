---
title: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 920
url: /fr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe d'un objet OLE incorporé. Les identifiants de classe d'objet Ole sont en fait des GUID, c'est-à-dire des identifiants uniques globaux. Le GUID fait toujours 16 octets de long, donc les identifiants de classe font également 16 octets de long. Ils se trouvent souvent à l'intérieur du Registre Windows et fournissent des informations à l'application hôte sur la façon d'ouvrir l'objet OLE incorporé contenant diverses ressources incorporées à l'intérieur de l'application cliente.
## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**
La capture d'écran suivante montre l'identifiant de classe d'objet Ole, c'est-à-dire le GUID qui a été lu à partir du [fichier excel d'exemple](5473378.xls) contenant l'objet OLE PowerPoint incorporé.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Code d'exemple**
Veuillez consulter le code d'exemple suivant exécuté avec [le fichier Excel d'exemple](5473378.xls) et sa sortie console qui affiche l'*Identifiant de classe* de l'objet Ole c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui montré à l'intérieur de la capture d'écran.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Sortie console**
Il s'agit de la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
