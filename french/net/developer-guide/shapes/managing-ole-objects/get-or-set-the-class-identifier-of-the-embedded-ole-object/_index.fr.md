---
title: Obtenir ou définir l'identificateur de classe de l'objet OLE intégré
type: docs
weight: 200
url: /fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Scénarios d'utilisation possibles**
 Aspose.Cells fournit le[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)propriété que vous pouvez utiliser pour obtenir ou définir l'identifiant de classe de l'objet ole intégré. Les identificateurs de classe d'objets Ole sont en fait des GUID, c'est-à-dire des identificateurs globalement uniques. Le GUID a toujours une longueur de 16 octets, donc les identificateurs de classe ont également une longueur de 16 octets. Ils se trouvent souvent dans le registre Windows et fournissent des informations à l'application hôte sur la façon d'ouvrir un objet ole intégré contenant diverses ressources intégrées dans l'application cliente.
## **Obtenir ou définir l'identificateur de classe de l'objet OLE intégré**
 La capture d'écran suivante montre l'identifiant de classe d'objet Ole, c'est-à-dire le GUID qui a été lu à partir du[exemple de fichier excel](5115190.xls) contenant l'objet ole PowerPoint intégré.

![tâche : image_autre_texte](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Exemple de code**
 Veuillez consulter l'exemple de code suivant exécuté avec[exemple de fichier excel](5115190.xls)et sa sortie de console qui imprime l'identifiant de classe de l'objet Ole, c'est-à-dire le GUID. Le GUID imprimé est exactement le même que celui indiqué dans la capture d'écran.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Sortie console**
 Il s'agit de la sortie console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier excel](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
