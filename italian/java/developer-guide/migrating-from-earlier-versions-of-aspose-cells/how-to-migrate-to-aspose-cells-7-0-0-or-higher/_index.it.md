---
title: Come migrare a Aspose.Cells 7.0.0 o versioni successive
type: docs
weight: 10
url: /it/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

In questo articolo, abbiamo condiviso i notevoli cambiamenti nel API che sono stati effettuati in Aspose.Cells for Java 7.0.0 e versioni successive rispetto alle versioni precedenti di Aspose.Cells for Java. Questo articolo aiuterà gli utenti a migrare rapidamente dal vecchio API al nuovo API comprendendo le modifiche apportate e realizzandole nelle proprie applicazioni.

{{% /alert %}}

## **Notevoli modifiche per gli utenti esistenti**

Dal rilascio di Aspose.Cells for Java v7.0.0, abbiamo apportato alcune importanti modifiche a API e abbiamo aggiunto tutte quelle funzionalità che sono presenti in Aspose.Cells for .NET fino ad oggi. Quindi, sia Aspose.Cells for Java che .NET saranno confrontabili ora in termini di funzionalità e persino in termini di nomi di metodi e proprietà.

Simile all'approccio precedente, puoi semplicemente importare solo un'istruzione di importazione nella tua applicazione per recuperare tutte le classi, le interfacce, ecc.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Abbiamo rinominato alcuni set di API per pulire la struttura API in modo che corrisponda a Aspose.Cells for .NET. Ora abbiamo aggiunto alcune classi di raccolta e le abbiamo sostituite con classi di raccolta esistenti. La classe Like Worksheets è stata sostituita con**Raccolta di fogli di lavoro** . Allo stesso modo, la classe Shapes è stata sostituita con**Collezione Shape**. Tuttavia, la funzionalità delle classi non è stata influenzata, anzi migliorata.

Se desideri migrare al nuovo API, potrebbe essere necessario apportare le seguenti modifiche nella tua applicazione per far funzionare le cose da parte tua. L'elenco seguente contiene le modifiche apportate alle classi e anche ai rispettivi metodi.

## **Riepilogo delle modifiche allo API**

1) Raccolte nella versione 2.5.4 o precedente i cui nomi che terminano con 's' vengono rinominati. Nella versione 7.0.0 o successiva, le Raccolte sono denominate come:
ad esempio, Shapes (vecchio) -> ShapeCollection (nuovo), fogli di lavoro (vecchio) -> WorksheetCollection (nuovo), ..., ecc.

2) L'acquisizione dell'elemento dalla raccolta è stata modificata. Ad esempio, nella versione 2.5.4 o precedente lo facevamo come getXXX(int), nella versione 7.0.0 o successiva, ora lo facciamo come get(int):
ad esempio, Worksheets.getSheet(int) (Vecchio) -> WorksheetCollection.get(int) (Nuovo), ...ecc.

3) L'ottenimento della dimensione (numero di elementi) di una raccolta è cambiato. Nella v2.5.4 o precedente, lo facevamo con size(), nella v7.0.0 o successiva, ora lo facciamo con getCount():
Worksheets.size() (vecchio) -> WorksheetCollection.getCount() (nuovo), ..., ecc.

4) Metodi getter delle proprietà booleane nella versione 2.5.4 o precedente i cui nomi che iniziano con 'is' sono stati modificati. Nella v7.0.0 questi sono iniziati con "get":
ad esempio, PageSetup.isBlackAndWhite() (Vecchio) -> PageSetup.getBlackAndWhite() (Nuovo), ...,ecc.
