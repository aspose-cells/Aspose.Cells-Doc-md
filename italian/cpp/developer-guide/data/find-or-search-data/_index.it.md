---
title: Trova o cerca dati
type: docs
weight: 80
url: /it/cpp/find-or-search-data/
---
## **Trova o cerca dati**
È possibile utilizzare Aspose.Cells per trovare o cercare dati in vari modi utilizzando il seguente metodo. Questi metodi trovano i dati secondo i loro nomi.

- [TrovaNumero](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7f90de51db6984956b5ed0b33b73a111)
- [TrovaFormula](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae3a8a9cfe7f8dc84ea590a8472e194f1)
- [FindFormulaContains](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae8d2b8cdef52ef4e501502c4b905943f)
- [TrovaStringa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac3e27028cf708eba8efb0997f9c9048e)
- [FindStringContains](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4f863b51674f7b18cf20a344872ad704)
- [FindStringStartsWith](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa17f3d771e73731dd9f682f4ac359df)
- [FindStringEndsWith](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7d0c58798771b7bc220fb162c30f247b)

 Il codice di esempio seguente illustra l'utilizzo dei metodi precedenti utilizzando il[file excel di esempio](21266434.xlsx) come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](find-or-search-data_1.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-FindOrSearchData.cpp" >}}
## **Uscita console**
 Questo è l'output della console del codice di esempio precedente quando eseguito con il file given[file excel di esempio](21266434.xlsx).



{{< highlight "java" >}}

 Name of the cell containing the number 80: A8

Name of the cell containing formula =SUM(A5:A10): C6

Name of the cell containing the formula that contains CHA: C7

Name of the cell containing specified string: C8

Name of the cell containing the string that contains Two: C9

Name of the cell containing the string that starts with AAA: C10

Name of the cell containing the string that ends with BBB: C11

{{< /highlight >}}
