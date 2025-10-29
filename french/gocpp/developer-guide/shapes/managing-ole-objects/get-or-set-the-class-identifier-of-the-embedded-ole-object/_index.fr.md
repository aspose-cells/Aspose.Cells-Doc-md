---
title: Obtenir ou définir l identifiant de classe de l objet OLE intégré via Golang en C++
linktitle: Obtenir ou définir l identifiant de classe de l objet OLE incorporé
type: docs
weight: 200
url: /fr/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Apprenez comment obtenir ou définir l identifiant de classe des objets OLE intégrés en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit la propriété [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe de l'objet OLE intégré. Les identifiants de classe OLE sont en fait des GUID, c'est-à-dire des Identifiants Unique Globaux. Un GUID fait toujours 16 octets de long, donc les identifiants de classe le sont aussi. Ils se trouvent souvent dans le Registre Windows et fournissent des informations à l'application hôte sur la façon d'ouvrir les objets OLE intégrés contenant diverses ressources intégrées à l'intérieur de l'application cliente.

## **Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé**
La capture d'écran suivante montre l'identifiant de classe d'objet OLE, c'est-à-dire le GUID, qui a été lu à partir du [fichier Excel d'exemple](5115190.xls) contenant l'objet PowerPoint OLE intégré.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Code d'exemple**
Veuillez voir le code d'exemple ci-dessous exécuté avec le [fichier Excel d'exemple](5115190.xls) et sa sortie console qui affiche l'identifiant de classe de l'objet OLE, c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui montré dans la capture d'écran.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Sortie console**
Ceci est la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
