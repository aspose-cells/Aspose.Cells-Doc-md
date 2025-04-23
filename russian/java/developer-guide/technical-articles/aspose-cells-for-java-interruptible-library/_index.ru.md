---
title: Aspose.Cells for Java  Прерываемая библиотека
type: docs
weight: 1090
url: /ru/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java поддерживает прерывание процесса загрузки/сохранения при работе с большими файлами Excel. Иногда вам нужно прервать выполнение библиотек/компонентов. Это определенно улучшит эффективность и надежность ваших услуг/процессов. Вы можете надежно отказаться от конвертации, когда обнаружите, что это занимает слишком много времени. Это сэкономит использование процессора, оперативной памяти и т.д. Это означает, что вам не нужно предпринимать радикальные шаги, такие как выключение всего сервера, чтобы отменить конвертацию. 
{{% /alert %}}

## **Пример:**

Следующая программа показывает, как прервать процесс сохранения с помощью метода **InterruptMonitor.interrupt()**.

[**Java**]

{{< highlight java >}}

 //Create a new Workbook  

final Workbook wb = new Workbook();

// Get the Worksheets

WorksheetCollection wss = wb.getWorksheets();

// Run a loop to fill sheet cells with data

for (int i = 0; i < 50; i++) {

    Worksheet sheet = wss.get(wss.add());

    Cells cells = sheet.getCells();

    for (int row = 0; row < 5000; row++) {

        for (int col = 0; col < 10; col++) {

            cells.get(row, col).setValue(i * 5000 + row * 500 + col);

        }

    }

}

final InterruptMonitor monitor = new InterruptMonitor();

wb.setInterruptMonitor(monitor);

new Thread(new Runnable() {

    public void run() {

        try {

            Thread.sleep(Math.round(Math.random() * 3000));

        } catch (InterruptedException e) {

        }

        // Interrupt the process

        monitor.interrupt();

        System.out.println("Interrupting the save thread at "

                + System.currentTimeMillis());

    }

}).start();

try {

    wb.save("makeinterrupted.xlsx", FileFormatType.XLSX);

} catch (CellsException e) {

    if (e.getCode() == ExceptionType.INTERRUPTED) {

        System.out.println(e.getMessage());

        System.out.println("The save thread finishes at "

                + System.currentTimeMillis());

    } else {

        throw e;

    }

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
