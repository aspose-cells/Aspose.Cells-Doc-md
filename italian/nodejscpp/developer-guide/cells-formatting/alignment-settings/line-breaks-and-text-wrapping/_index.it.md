---  
title: Interruzioni di riga e a capo automatico del testo
linktitle: Interruzioni di riga e a capo automatico del testo  
description: Come implementare l andatura del testo e il word wrap usando la libreria Aspose.Cells in Node.js tramite C++. Utilizzando la libreria Aspose.Cells, puoi inserire facilmente il testo nelle celle e impostare il metodo di avvolgimento del testo, come word wrap manuale, word wrap, ecc. Questo documento illustra come implementare queste funzionalità e fornisce codice di esempio per il tuo riferimento.  
keywords: Aspose.Cells, interruzioni di riga, word wrap, layout del testo Node.js tramite C++  
type: docs  
weight: 60  
url: /it/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.  
{{% /alert %}}  

## **Per incapsulare il testo in una cella**  
Per avvolgere il testo in una cella, usa il metodo [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Per utilizzare ritorni a capo espliciti**  
Puoi usare ‘\n’ in JavaScript per inserire interruzioni di riga esplicite in una cella.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



