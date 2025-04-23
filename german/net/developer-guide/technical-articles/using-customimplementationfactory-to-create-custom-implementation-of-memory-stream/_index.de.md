---
title: Verwendung von CustomImplementationFactory zur Erstellung einer benutzerdefinierten Implementierung des MemoryStream
type: docs
weight: 40
url: /de/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells hat eine API namens [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory), die es dem Benutzer ermöglicht, benutzerdefinierte Implementierungen wie die Verwendung der Recyclable-Speicherimplementierung anstelle des Standard-MemoryStream zu verwenden.

## **Verwendung von CustomImplementationFactory zur Erstellung einer benutzerdefinierten Implementierung des MemoryStream**

Der folgende Beispielcode veranschaulicht, wie man [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) in Ihrem Programm verwendet. Manchmal gibt es genügend Speicher in Ihrem System, aber der Speicher ist nicht zusammenhängend. MemoryStream-Objekte verwenden zusammenhängenden Speicher, aber Sie können die Implementierung von MemoryStream so bereitstellen, dass sie stattdessen nicht zusammenhängenden Speicher verwendet.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
{{< app/cells/assistant language="csharp" >}}
