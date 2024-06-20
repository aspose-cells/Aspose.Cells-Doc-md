---
title: Utilisation de CustomImplementationFactory pour créer une implémentation personnalisée de Memory Stream
type: docs
weight: 40
url: /fr/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells a fourni une API nommée [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) qui permet à l'utilisateur de fournir une implémentation personnalisée telle que l'utilisation d'une implémentation de mémoire recyclable au lieu du MemoryStream par défaut.

## **Utilisation de CustomImplementationFactory pour créer une implémentation personnalisée de Memory Stream**

L'exemple de code suivant illustre comment utiliser [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) dans votre programme. Parfois, il y a suffisamment de mémoire dans votre système mais la mémoire n'est pas contiguë. Les objets Memory Stream utilisent une mémoire contiguë mais vous pouvez fournir l'implémentation de Memory Stream de telle manière qu'elle utilise plutôt une mémoire non contiguë.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
