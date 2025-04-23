---
title: Éditeur de feuilles de calcul  Travailler avec des fichiers
type: docs
weight: 10
url: /fr/java/spreadsheet-editor-working-with-files/
---

**Table des matières**

- [Fichiers pris en charge](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Ouvrir des fichiers locaux](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Ouvrir depuis Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Ouvrir depuis une URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Créer un nouveau Spreadsheet](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Exporter vers divers formats](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Fichiers pris en charge**
L'éditeur de feuilles de calcul HTML5 peut ouvrir des fichiers dans les formats suivants :

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Ouvrir des fichiers locaux**
Pour télécharger un fichier depuis l'ordinateur local :

1. Passer à l'onglet **Fichier** en haut.
2. Cliquez sur **Ouvrir depuis l'ordinateur** pour ouvrir la boîte de dialogue Parcourir.
1. Allez à l'emplacement de fichier souhaité.
1. Sélectionnez le fichier souhaité en cliquant dessus.
1. Cliquez sur **Ouvrir**.

Le fichier sera ouvert dans l'éditeur.

![todo:image_alt_text](bwyl3xi.png)

**Comment cela fonctionne?**

**Téléchargement de fichier**

L'utilisateur sélectionne un fichier depuis son ordinateur local, qui est téléchargé du navigateur web vers le serveur et reçu par le composant [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml).

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestion du classeur**

Dès que le fichier est complètement téléchargé, la méthode WorkbookService.onFileUpload entre en action pour gérer la situation. WorkbookService reçoit des événements du navigateur web et surveille l'état du classeur. WorkbookService.onFileUpload transmet le contrôle à LoaderService pour charger le classeur en mémoire. Comme le composant ***fileUpload*** fournit le fichier téléchargé sous forme de [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService le charge à l'aide de la méthode LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Chargement et déchargement**

La méthode ***LoaderService.fromInputStream*** lit le ***InputStream*** fourni par le composant de téléchargement de fichier pour créer une instance de la classe ***com.aspose.cells.Workbook***. Cette instance est conservée en mémoire tant que l'utilisateur continue de consulter ou de modifier la feuille de calcul dans le navigateur web. Lorsque l'utilisateur quitte l'éditeur ou ferme le navigateur, les instances inutilisées sont automatiquement déchargées de la mémoire pour maintenir le serveur propre.







{{< highlight java >}}

 public String fromInputStream(InputStream s, String name) {

    com.aspose.cells.Workbook w;

    try (InputStream i = s) {

        w = new com.aspose.cells.Workbook(i);

    } catch (Exception x) {

        return null;

    }

    String key = this.generateKey();

    this.workbooks.put(key, w);

    this.buildCellsCache(key);

    this.buildColumnWidthCache(key);

    this.buildRowHeightCache(key);

    return key;

}

{{< /highlight >}}







**Mise en cache**

La mise en cache est très importante pour l'éditeur de feuilles de calcul HTML5. Elle permet de garantir un fonctionnement fluide. Le CellsService conserve en cache les lignes, les colonnes, les cellules et les propriétés de tous les classeurs chargés par l'éditeur. Lorsque LoaderService charge une feuille de calcul complètement, il lit celle-ci de haut en bas et remplit le cache en appelant LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache.







{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **LoaderService.buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **LoaderService.buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Ouvrir depuis Dropbox**
Pour ouvrir des fichiers depuis Dropbox:

1. Passer à l'onglet **Fichier** en haut.
1. Cliquez sur **Ouvrir depuis Dropbox** pour ouvrir le sélecteur de fichiers Dropbox.
1. Si vous n'êtes pas déjà connecté, il vous sera demandé de vous connecter à votre compte Dropbox.
1. Naviguez jusqu'au fichier souhaité et cliquez pour le sélectionner.
1. Cliquez sur **Choisir** en bas.

Le fichier sélectionné sera ouvert depuis Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**Comment cela fonctionne?**

Le bouton **Ouvrir depuis Dropbox** utilise l'API de Chooser de JavaScript Dropbox pour ouvrir la boîte de dialogue Dropbox Chooser. Le Chooser fournit l'URL du fichier sélectionné, qui est capturée par la fonction de rappel et renvoyée au serveur. Le serveur crée une instance du spreadsheet à partir de l'URL, initialise quelques tâches de maintenance, et renvoie des mises à jour DOM au navigateur. Le navigateur rend et rafraîchit l'HTML et l'utilisateur est prêt à éditer le document chargé.
### **Ouvrir depuis une URL**
Les fichiers peuvent être directement ouverts depuis des URLs. Cela permet à l'utilisateur d'éditer n'importe quel fichier disponible publiquement sur Internet. Pour ouvrir le fichier, ajoutez le paramètre **?url=emplacement** avec la valeur de votre **emplacement** souhaité lors du chargement de l'éditeur. Par exemple :

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Comment cela fonctionne?**

**Instanciation lors du démarrage**

Lors de l'instanciation du bean backend **WorksheetView** par JSF, la méthode **PostConstruct** **init** est appelée pour charger le spreadsheet à l'aide de LoaderService.fromUrl.

**Mise en cache**

La mise en cache se produit juste après le chargement de la feuille de calcul. **LoaderService** appelle **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** et **LoaderService.buildRowHeightCache** l'un après l'autre pour mettre en cache le contenu de la feuille de calcul et maintenir toutes les opérations rapides et fluides.

**Mises à jour du DOM**

Une fois que la feuille de calcul est prête du côté serveur, des composants JSF sont utilisés pour générer un nouveau HTML et envoyer des mises à jour du DOM à l'utilisateur, qui sont rendues par le navigateur Web.







{{< highlight java >}}

     @PostConstruct

    private void init() {

        String requestedSourceUrl = FacesContext.getCurrentInstance().getExternalContext().getRequestParameterMap().get("url");

        if (requestedSourceUrl != null) {

            try {

                this.sourceUrl = new URL(requestedSourceUrl).toString();

                this.loadFromUrl();

            } catch (MalformedURLException x) {

                msg.sendMessageDialog("The specified URL is invalid", requestedSourceUrl);

            }

        }

    }

{{< /highlight >}}




#### **LoaderService.fromUrl**
{{< highlight java >}}

     public String fromUrl(String url) {

        com.aspose.cells.Workbook w;

        try (InputStream i = new URL(url).openStream()) {

            w = new com.aspose.cells.Workbook(i);

        } catch (Exception x) {

            throw new RuntimeException(x);

        }

        String key = generateKey();

        workbooks.put(key, w);

        buildCellsCache(key);

        buildColumnWidthCache(key);

        buildRowHeightCache(key);

        return key;

    }

{{< /highlight >}}




#### **LoaderService.buildCellsCache**
{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **LoaderService.buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **LoaderService.buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Créer un nouveau Spreadsheet**
Pour créer un nouveau spreadsheet vide :

1. Passer à l'onglet **Fichier**.
1. Cliquez sur le bouton **Nouveau**.

L'éditeur fermera la feuille de calcul ouverte, le cas échéant, et ouvrira une nouvelle.

![todo:image_alt_text](lnydmmf.png)

**Comment cela fonctionne?**

**Instancier un nouvel objet**

Lorsque l'utilisateur clique sur le bouton **Nouveau**, **WorksheetView.loadBlank** est appelé, ce qui appelle finalement **LoaderService.fromBlank**. LoaderService crée une nouvelle instance de feuille de calcul vierge.

**Mise en cache**

La mise en cache se produit juste après le chargement de la feuille de calcul. **LoaderService** appelle **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** et **LoaderService.buildRowHeightCache** l'un après l'autre pour mettre en cache le contenu de la feuille de calcul et maintenir toutes les opérations rapides et fluides.

**Mises à jour du DOM**

Une fois que la feuille de calcul est prête du côté serveur, des composants JSF sont utilisés pour générer un nouveau HTML et envoyer des mises à jour du DOM à l'utilisateur, qui sont rendues par le navigateur Web.







{{< highlight java >}}

     public void loadBlank() {

        this.loadedWorkbook = loader.fromBlank();

    }

{{< /highlight >}}




#### **LoaderService.fromBlank**
{{< highlight java >}}

     public String fromBlank() {

        com.aspose.cells.Workbook w = new com.aspose.cells.Workbook();

        String key = generateKey();

        workbooks.put(key, w);

        buildCellsCache(key);

        buildColumnWidthCache(key);

        buildRowHeightCache(key);

        return key;

    }

{{< /highlight >}}




#### **buildCellsCache**
{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Exporter vers divers formats**
Après avoir modifié des fichiers, l'utilisateur voudra enregistrer les modifications. L'éditeur permet à l'utilisateur d'exporter et de télécharger la feuille de calcul modifiée sur son ordinateur local. Pour exporter le fichier :

1. Passer à l'onglet **Fichier** en haut.
1. Cliquez sur le bouton **Exporter sous**.
1. Choisissez le format désiré dans la liste déroulante.

Le fichier modifié sera exporté pour téléchargement. Les formats suivants sont pris en charge pour l'export :

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Format de document portable (PDF)
- OpenDocument Spreadsheet (ODS)

**Comment cela fonctionne?**

La feuille de calcul ouverte est convertie au format spécifié par l'utilisateur en utilisant **WorksheetView.getOutputFile**.







{{< highlight java >}}

     public StreamedContent getOutputFile(int saveFormat) {

        byte[] buf;

        String ext = null;

        switch (saveFormat) {

            case com.aspose.cells.SaveFormat.EXCEL_97_TO_2003:

                ext = "xls";

                break;

            case com.aspose.cells.SaveFormat.XLSX:

                ext = "xlsx";

                break;

            case com.aspose.cells.SaveFormat.XLSM:

                ext = "xlsm";

                break;

            case com.aspose.cells.SaveFormat.XLSB:

                ext = "xlsb";

                break;

            case com.aspose.cells.SaveFormat.XLTX:

                ext = "xltx";

                break;

            case com.aspose.cells.SaveFormat.XLTM:

                ext = "xltm";

                break;

            case com.aspose.cells.SaveFormat.SPREADSHEET_ML:

                ext = "xml";

                break;

            case com.aspose.cells.SaveFormat.PDF:

                ext = "pdf";

                break;

            case com.aspose.cells.SaveFormat.ODS:

                ext = "ods";

                break;

        }

        try {

            ByteArrayOutputStream out = new ByteArrayOutputStream();

            getAsposeWorkbook().save(out, saveFormat);

            buf = out.toByteArray();

        } catch (Exception x) {

            throw new RuntimeException(x);

        }

        return new DefaultStreamedContent(new ByteArrayInputStream(buf), "application/octet-stream", "Spreadsheet." + ext);

    }

{{< /highlight >}}






{{< app/cells/assistant language="java" >}}
