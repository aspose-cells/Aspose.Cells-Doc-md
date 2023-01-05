---
title: Aspose.Cells for Java - Прерываемая библиотека
type: docs
weight: 1090
url: /ru/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java поддерживает прерывание процесса загрузки/сохранения при работе с большими файлами Excel. Иногда вы хотите сделать библиотеки/компоненты прерываемыми. Это, безусловно, повысит эффективность и надежность ваших услуг/процессов. Вы можете надежно отказаться от преобразования на полпути, когда обнаружите, что оно занимает слишком много времени. Это сэкономит ресурсы ЦП, ОЗУ и т. д. Это означает, что вам не нужно предпринимать радикальные шаги, такие как уничтожение всего сервера только для того, чтобы отменить преобразование.
{{% /alert %}}

## **Пример:**

 Следующая программа показывает, как прервать процесс сохранения с помощью**InterruptMonitor.interrupt()** метод.

[**Java**]{{< highlight "java" >}}

 //Создаем новую книгу

окончательная рабочая книга wb = новая рабочая книга();

// Получить рабочие листы

Коллекция рабочих листов wss = wb.getWorksheets();

// Запуск цикла для заполнения ячеек листа данными

 для (целое я = 0; я< 50; i++) {

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
