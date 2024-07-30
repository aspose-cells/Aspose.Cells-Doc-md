---
title: Bloccare o sbloccare forme
linktitle: Bloccare o sbloccare forme
type: docs
weight: 200
url: /it/net/lock-or-unlock-shapes/
description: Questo articolo mostra del codice che spiega come Bloccare o sbloccare forme per proteggerle utilizzando la libreria Aspose.Cells.
keywords: C# Blocca Forme per Proteggerle, Come Bloccare o sbloccare forme usando C#, Bloccare o sbloccare forme per Proteggerle in C#.
---

## **Possibili Scenari di Utilizzo**

A volte è necessario proteggere tutte le forme in determinati fogli di lavoro per evitare che vengano distrutte da situazioni indesiderate. In questo caso, è necessario bloccare tutte le forme nel foglio di lavoro specificato. 

Il blocco delle forme in un foglio di calcolo o documento può essere vantaggioso per diversi motivi:
1. Prevenire Modifiche Accidentali: Il blocco delle forme garantisce che non vengano spostate, ridimensionate o eliminate accidentalmente dagli utenti. Questo è particolarmente importante in documenti complessi in cui le forme possono essere utilizzate per annotazioni, illustrazioni o come parte del design del documento.
1. Mantenere il Layout e il Design: Le forme spesso giocano un ruolo cruciale nel layout e nel design visivo di un documento. Bloccarle preserva l'aspetto previsto, garantendo che il documento rimanga professionale e esteticamente accattivante.
1. Integrità dei Dati: Nei fogli di calcolo, le forme possono essere utilizzate per evidenziare punti dati importanti, aggiungere commenti o fornire spiegazioni visive. Bloccare queste forme assicura che le informazioni contestuali che forniscono rimangano accurate e integre.
1. Coerenza nei Documenti Condivisi: Quando si collabora ai documenti, diversi utenti potrebbero avere livelli di competenza diversi. Il blocco delle forme aiuta a mantenere la coerenza nel documento evitando modifiche non intenzionali.
1. Sicurezza: Nei documenti sensibili, bloccare le forme può far parte di una strategia più ampia per proteggere le informazioni. Ad esempio, nei rapporti finanziari o nei documenti legali, le forme bloccate possono essere utilizzate per salvaguardare annotazioni specifiche o evidenziare che forniscono contesti critici.

A volte, potresti dover essere in grado di modificare determinate forme in fogli di lavoro protetti, in tal caso, è necessario sbloccare queste forme. Questo articolo illustrerà in dettaglio come bloccare e sbloccare forme specifiche.

## **Come Bloccare le Forme per Proteggerle in Excel**

Ecco come puoi bloccare le celle in Microsoft Excel:

1. Apri il tuo file di Excel: Apri il file di Excel che contiene le forme che desideri bloccare.

1. Seleziona la Forma: Fai clic sulla forma che desideri bloccare. È anche possibile selezionare più forme tenendo premuto il tasto Ctrl e facendo clic su ciascuna forma.

1. Apri il Pannello Formato Forma: Fai clic con il tasto destro sulla/e forma/e selezionata/e e scegli "Dimensioni e proprietà." In alternativa, è possibile andare alla scheda "Formato" sul Nastro e nel gruppo "Dimensioni", fare clic sul lanciatore di dialogo (una piccola freccia) per aprire il pannello "Formato Forma".
1. Blocca la Forma: Nel pannello "Formato Forma", vai alla scheda "Dimensioni e proprietà" (l'icona assomiglia a un quadrato con frecce). Nella sezione "Proprietà", seleziona la casella "Bloccato".
<br>
<img src="1.png" width=60% />
1. Proteggi il Foglio di Lavoro: Vai alla scheda "Revisione" nel Ribbon. Clicca su "Proteggi foglio". Imposta una password (opzionale) e scegli i permessi che vuoi concedere (es. selezionare celle bloccate, formattare celle, etc.). Clicca su "OK".
<br>
<img src="2.png" width=60% />

## **Come Bloccare tutte le forme in un determinato foglio di lavoro**

Per proteggere tutte le forme in un determinato foglio di lavoro, utilizzare il metodo [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), come mostrato nel seguente codice di esempio.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Come Sbloccare forme specifiche in un foglio di lavoro protetto**

Per sbloccare una forma specifica in un foglio di lavoro protetto, utilizzare [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), come mostrato nel seguente codice di esempio.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ha significato solo quando il foglio di lavoro è protetto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

