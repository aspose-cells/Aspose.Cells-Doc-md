---
title: Verwenden von CustomImplementationFactory zum Erstellen einer benutzerdefinierten Implementierung von Memory Stream
type: docs
weight: 40
url: /de/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Mögliche Nutzungsszenarien**

 Aspose.Cells hat eine API mit dem Namen bereitgestellt[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)Dadurch kann der Benutzer eine benutzerdefinierte Implementierung bereitstellen, z. B. die Verwendung einer recyclebaren Speicherimplementierung anstelle des Standard-MemoryStream.

## **Verwenden von CustomImplementationFactory zum Erstellen einer benutzerdefinierten Implementierung von Memory Stream**

Der folgende Beispielcode veranschaulicht die Verwendung von[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)in deinem Programm. Manchmal ist in Ihrem System genügend Speicher vorhanden, aber der Speicher ist nicht zusammenhängend. Memory Stream-Objekte verwenden zusammenhängenden Speicher, aber Sie können die Implementierung von Memory Stream so bereitstellen, dass stattdessen der nicht zusammenhängende Speicher verwendet wird.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
