---
title: Come migrare ad Aspose.Cells 7.0.0 o superiore
type: docs
weight: 10
url: /it/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

In questo articolo sono state condivise le modifiche degne di nota nell'API che sono state apportate nella versione 7.0.0 e successive rispetto alle versioni predecessore di Aspose.Cells for Java. Questo articolo aiuterà gli utenti a migrare rapidamente dall'API vecchia alla nuova API comprendendo le modifiche apportate e applicandole alle proprie applicazioni.

{{% /alert %}}

## **Modifiche degne di nota per gli utenti esistenti**

Dalla release di Aspose.Cells for Java v7.0.0, abbiamo apportato alcune modifiche importanti all'API e abbiamo aggiunto tutte quelle funzionalità presenti in Aspose.Cells for .NET fino a oggi. Quindi, sia Aspose.Cells for Java che .NET saranno confrontabili ora in termini di funzionalità e anche in termini di nomi dei metodi e delle proprietà.

Come nell'approccio precedente, è possibile importare solo un'unica dichiarazione di importazione nella propria applicazione per recuperare tutte le classi, interfacce, ecc.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Abbiamo rinominato alcune API per pulire la struttura dell'API in modo da farla corrispondere a Aspose.Cells for .NET. Abbiamo ora aggiunto alcune classi di raccolta e le abbiamo sostituite con le classi di raccolta esistenti. Ad esempio, la classe Worksheets è stata sostituita con **WorksheetCollection**. Allo stesso modo, la classe Shapes è stata sostituita con **ShapeCollection**. Tuttavia, la funzionalità delle classi non è stata modificata, ma migliorata.

Se si desidera migrare alla nuova API, potrebbe essere necessario apportare le seguenti modifiche alla propria applicazione per far funzionare le cose sul proprio sistema. L'elenco seguente contiene le modifiche apportate alle classi e ai rispettivi metodi.

## **Sommario delle modifiche nell'API**

1) Le raccolte in v2.5.4 o precedenti il cui nome termina con 's' sono rinominate. In v7.0.0 o successive, le raccolte sono denominate come:
ad esempio, Shapes (Vecchio) -> ShapeCollection (Nuovo), Worksheets (Vecchio) -> WorksheetCollection (Nuovo), ...,ecc.

2) Ottenere l'elemento dalla raccolta è cambiato. Ad esempio, in v2.5.4 o precedenti usavamo getXXX(int), in v7.0.0 o superiore, ora lo facciamo come get(int):
ad esempio, Worksheets.getSheet(int) (Vecchio) -> WorksheetCollection.get(int) (Nuovo), ...ecc.

3) Ottenere la dimensione (conteggio degli elementi) di una raccolta è cambiato. In v2.5.4 o precedenti, lo facevamo con size(), in v7.0.0 o superiore, ora lo facciamo con getCount():
Worksheets.size() (Vecchio) -> WorksheetCollection.getCount() (Nuovo), ...ecc.

4) I metodi getter delle proprietà booleane nella v2.5.4 o precedenti il cui nome inizia con 'is' sono stati modificati. In v7.0.0 questi inizieranno con "get":
ad es., PageSetup.isBlackAndWhite() (Vecchio) -> PageSetup.getBlackAndWhite() (Nuovo), ...,ecc.
