---
title: Come installare un font su Linux
type: docs
description: "Come installare un font su Linux"
weight: 139
url: /it/net/how-to-install-font-in-linux/
---

## Panoramica

Quando si utilizza Aspose.Cells su Linux, poiché Linux ha meno font predefiniti, il font referenziato nel file Excel potrebbe non esistere di default nel sistema Linux.
Quando ciò accade, Aspose.Cells utilizzerà un font simile per mostrare i caratteri. Tuttavia, questo può causare i seguenti effetti:

1. Font diversi possono comportare immagini visualizzate in layout diversi rispetto a Excel.
2. Poiché il font è cambiato, i caratteri di output potrebbero non essere di tuo gradimento.

Per ottenere risultati più accurati, installa i font necessari su Linux. È importante assicurarsi che i font usati nei file Excel esistano nel tuo ambiente.

## Come installare font su Linux

Ci sono due modi per installare i font su Linux, come descritto di seguito:

### Copiare i file dei font nel percorso di sistema di Linux

1. Metti una cartella chiamata "fonts" nella directory del tuo programma, copia al suo interno i file font necessari.
2. Aggiungi il comando seguente al tuo Dockerfile Linux:
```
COPY fonts/ /usr/share/fonts
```
3. Dopo l'operazione sopra, i file dei font verranno copiati nel percorso di sistema Linux. Aspose.Cells accederà al percorso di sistema e li troverà e userà. Questo è il nostro scenario raccomandato.

### Imposta cartella font con API Aspose.Cells
In alcuni casi, potresti non essere in grado di controllare o modificare la directory di sistema Linux. Per esempio, sui server cloud. In questo caso, puoi usare il secondo scenario.
1. Inserisci una cartella nominata "fonts" nella directory del tuo programma e copia i file font necessari in questa cartella.
2. Nel codice del tuo programma, chiama l'API di Aspose.Cells:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. L'operazione sopra assicurerà che il programma possa trovare i font dal percorso del progetto.

## Vedi Anche

- [Come eseguire Aspose.Cells per .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
