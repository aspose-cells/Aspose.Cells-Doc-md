---
title: Come Usare i Markers Immagine in Smart Markers
type: docs
weight: 30
url: /it/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Possibili Scenari di Utilizzo**
Gli indicatori di immagine sono segnaposto specializzati nei sistemi di templating (come FoxPro, Handlebars o framework UI moderni) che iniettano dinamicamente immagini o asset visivi nei modelli. A volte, è necessario inserire immagini usando smart markers. Aspose.Cells permette di aggiungere immagini ai smart markers.

## **Image Parameters in Smart Markers**
Parametri smart marker per gestire le immagini.

- **Immagine: AdattaACella** - Adatta automaticamente l'immagine all'altezza della riga e alla larghezza della colonna della cella.
- **Immagine: ScalaN** - Scala altezza e larghezza al N percento.
- **Immagine: Larghezza:Npollici&Altezza:Npollici** - Rappresenta l'immagine alta N pollici e larga N pollici. È inoltre possibile specificare le posizioni Sinistra e Alto (in punti).

## **Come usare i marker immagine in Smart Markers**
Vedi il seguente esempio di codice che mostra come inserire immagini utilizzando i marker intelligenti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Come usare i marker immagine durante il raggruppamento dei dati in Smart Markers**
Il codice di esempio seguente crea un foglio di lavoro e poi aggiunge i seguenti tag del marker intelligente nelle celle D2, E2 e F2 rispettivamente

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Successivamente riempie l'origine dati con dati e chiama il metodo [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) per processare i tag del marker intelligente. Il codice utilizza queste immagini ossia [moon.png](5115492.png) e [moon2.png](5115491.png) ma è possibile utilizzare qualsiasi immagine

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
