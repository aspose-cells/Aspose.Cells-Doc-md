---
title: Éditeur de feuille de calcul - Travailler avec des fichiers
type: docs
weight: 10
url: /fr/java/spreadsheet-editor-working-with-files/
---
**Table des matières**

- [Fichiers pris en charge](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Ouvrir les fichiers locaux](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Ouvrir depuis Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Ouvrir à partir de l'URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Créer une nouvelle feuille de calcul](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [Exporter vers divers formats](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Fichiers pris en charge**
HTML5 Spreadsheet Editor peut ouvrir des fichiers dans les formats suivants :

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- TableurML
- SVC
- OuvrirDocument
### **Ouvrir les fichiers locaux**
Pour télécharger un fichier depuis un ordinateur local :

1.  Basculer vers**Onglet Fichier** en haut.
1.  Cliquez sur**Ouvrir à partir de l'ordinateur** pour ouvrir la boîte de dialogue Parcourir.
1. Accédez à l'emplacement de fichier souhaité.
1. Cliquez sur le fichier souhaité pour le sélectionner.
1.  Cliquez sur**Ouvert**.

Le fichier sera ouvert dans l'éditeur.

![tâche : image_autre_texte](bwyl3xi.png)

**Comment ça fonctionne?**

**Téléchargement de fichiers**

 L'utilisateur sélectionne un fichier à partir de l'ordinateur local qui est téléchargé du navigateur Web vers le serveur et reçu par[Fichier PrimeFacesTélécharger](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) composant.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestion du classeur**

 Dès que le fichier est téléchargé complètement, la méthode WorkbookService.onFileUpload entre en action pour gérer la situation. WorkbookService reçoit les événements du navigateur Web et suit l'état de l'ensemble du classeur. Le WorkbookService.onFileUpload transmet le contrôle à LoaderService pour charger le classeur en mémoire. Comme le***téléchargement de fichiers*** Le composant fournit le fichier téléchargé en tant que[Flux d'entrée](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), le LoaderService le charge à l'aide de la méthode LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Chargement et déchargement**

 La méthode***LoaderService.fromInputStream*** lit le***Flux d'entrée*** fourni par fileUpload***composant*** créer une instance de***com.aspose.cells.Workbook***classer. Cette instance est conservée en mémoire tant que l'utilisateur continue d'afficher ou de modifier la feuille de calcul dans le navigateur Web. Lorsque l'utilisateur quitte l'éditeur ou ferme le navigateur, les instances inutilisées sont automatiquement déchargées de la mémoire pour garder le serveur propre.







{{< highlight "java" >}}

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

La mise en cache est très importante pour HTML5 Spreadsheet Editor. Cela fait que tout fonctionne en douceur. Le CellsService conserve les lignes, les colonnes, les cellules et les propriétés du cache de tous les classeurs chargés par l'éditeur. Lorsque LoaderService charge complètement une feuille de calcul, il la lit de haut en bas et remplit le cache en appelant LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
Pour ouvrir des fichiers depuis Dropbox :

1.  Basculer vers**Onglet Fichier** en haut.
1.  Cliquez sur**Ouvrir depuis Dropbox** pour ouvrir le sélecteur de fichiers Dropbox.
1. Si vous n'êtes pas déjà connecté, vous devrez vous connecter à votre compte Dropbox.
1. Naviguez jusqu'au fichier souhaité et cliquez dessus pour le sélectionner.
1.  Cliquez sur**Choisir** au fond.

Votre fichier sélectionné sera ouvert à partir de Dropbox.

![tâche : image_autre_texte](1e2sfo0.png)

**Comment ça fonctionne?**

 La**Ouvrir depuis Dropbox** bouton utilise**Sélecteur JavaScript Dropbox API** pour ouvrir la boîte de dialogue Sélecteur de Dropbox. Le sélecteur fournit l'URL du fichier sélectionné, qui est capturé par la fonction de rappel et renvoyé au serveur. Le serveur crée une instance de feuille de calcul à partir de l'URL, initialise certains éléments d'entretien et renvoie les mises à jour DOM au navigateur. Le navigateur affiche et actualise le code HTML et l'utilisateur est prêt à modifier le document chargé.
### **Ouvrir à partir de l'URL**
 Les fichiers peuvent être ouverts directement à partir d'URL. Cela permet à l'utilisateur de modifier n'importe quel fichier accessible au public sur Internet. Pour ouvrir le fichier ajouter**?url=emplacement** paramètre avec la valeur de votre choix**emplacement** lors du chargement de l'éditeur. Par exemple:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![tâche : image_autre_texte](exc9ckp.png)

**Comment ça fonctionne?**

**Instancier au démarrage**

 Lorsque**Feuille de calcul** le bean backend est instancié par JSF le**Post-construction** méthode**initialiser** est appelé qui charge la feuille de calcul à l'aide de LoaderService.fromUrl.

**Mise en cache**

 La mise en cache se produit juste après le chargement de la feuille de calcul. La**LoaderService** appels**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** et**LoaderService.buildRowHeightCache** un par un pour mettre en cache le contenu de la feuille de calcul et maintenir toutes les opérations rapides et fluides.

**Mises à jour DOM**

Lorsque la feuille de calcul est prête côté serveur, les composants JSF sont utilisés pour générer un nouveau HTML et envoyer des mises à jour DOM à l'utilisateur qui sont rendues par le navigateur Web.







{{< highlight "java" >}}

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




#### **LoaderService.fromUrlLoaderService.fromUrl**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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






### **Créer une nouvelle feuille de calcul**
Pour créer une nouvelle feuille de calcul vide :

1.  Basculer vers**Onglet Fichier**.
1.  Clique le**Nouveau** bouton.

L'éditeur fermera la feuille de calcul ouverte, le cas échéant, et en ouvrira une nouvelle.

![tâche : image_autre_texte](lnydmmf.png)

**Comment ça fonctionne?**

**Instancier un nouvel objet**

 Quand le**Nouveau** le bouton est cliqué par l'utilisateur,**WorksheetView.loadBlankWorksheetView.loadBlank** , qui finit par appeler**LoaderService.fromBlank**. LoaderService crée une nouvelle instance de feuille de calcul vierge.

**Mise en cache**

 La mise en cache se produit juste après le chargement de la feuille de calcul. La**LoaderService** appels**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** et**LoaderService.buildRowHeightCache** un par un pour mettre en cache le contenu de la feuille de calcul et maintenir toutes les opérations rapides et fluides.

**Mises à jour DOM**

Lorsque la feuille de calcul est prête côté serveur, les composants JSF sont utilisés pour générer un nouveau HTML et envoyer des mises à jour DOM à l'utilisateur qui sont rendues par le navigateur Web.







{{< highlight "java" >}}

     public void loadBlank() {

        this.loadedWorkbook = loader.fromBlank();

    }

{{< /highlight >}}




#### **LoaderService.fromBlank**
{{< highlight "java" >}}

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




#### **buildCellsCachebuildCellsCache**
{{< highlight "java" >}}

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




#### **buildColumnWidthCachebuildColumnWidthCache**
{{< highlight "java" >}}

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




#### **buildRowHeightCachebuildRowHeightCache**
{{< highlight "java" >}}

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
Après avoir modifié les fichiers, l'utilisateur voudra enregistrer les modifications. L'éditeur permet à l'utilisateur d'exporter et de télécharger la feuille de calcul modifiée sur l'ordinateur local. Pour exporter le fichier :

1.  Basculer vers**Onglet Fichier** en haut.
1.  Cliquez sur**Exporter** comme bouton.
1. Choisissez le format souhaité dans la liste déroulante.

Le fichier modifié sera exporté pour téléchargement. Les formats suivants sont pris en charge pour l'exportation :

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLMC
- TableurML
- Format de document portable (PDF)
- Feuille de calcul OpenDocument (ODS)

**Comment ça fonctionne?**

 La feuille de calcul ouverte est convertie au format spécifié par l'utilisateur à l'aide de**WorksheetView.getOutputFileWorksheetView.getOutputFile**.







{{< highlight "java" >}}

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






