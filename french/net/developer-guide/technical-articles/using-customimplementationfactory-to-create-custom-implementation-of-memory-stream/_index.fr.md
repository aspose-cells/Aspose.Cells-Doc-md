---
title: Utilisation de CustomImplementationFactory pour créer une implémentation personnalisée de Memory Stream
type: docs
weight: 40
url: /fr/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells a fourni un API nommé[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)qui permet à l'utilisateur de fournir une implémentation personnalisée telle que l'utilisation de l'implémentation de la mémoire recyclable au lieu du MemoryStream par défaut.

## **Utilisation de CustomImplementationFactory pour créer une implémentation personnalisée de Memory Stream**

L'exemple de code suivant illustre l'utilisation de[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)dans votre programme. Parfois, il y a suffisamment de mémoire dans votre système mais la mémoire n'est pas contiguë. Les objets Memory Stream utilisent de la mémoire contiguë mais vous pouvez fournir l'implémentation de Memory Stream de manière à ce qu'il utilise à la place la mémoire non contiguë,

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
