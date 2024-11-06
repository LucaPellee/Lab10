import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.ddCountry = None


    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self.annoStr = self._view._txtAnno.value
        try:
            self.anno = int(self.annoStr)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Inserire numero intero")
            self._view.update_page()
            return
        if self.anno < 1816 or self.anno > 2016:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Inserire anno tra 1816 e 2016")
            self._view.update_page()
            return

        self._model.creaGrafo(self.anno)
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view._txt_result.controls.append(ft.Text("Grafo creato"))
        self._view._txt_result.controls.append(ft.Text(f"Numero nodi: {nNodes}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero archi: {nEdges}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero componenti connesse: {self._model.getNumCompConnesse()}"))
        nodi = self._model.trovaNodi()
        for n in nodi:
            num = self._model.trovaNumArchiVicini(n)
            self._view._txt_result.controls.append(ft.Text(f"{n}-- {num} vicini"))
        self._view._ddStato.disabled = False
        self._view._btnRaggiungibili.disabled = False
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
        listaNodi = self._model.trovaNodi()
        for n in listaNodi:
            self._view._ddStato.options.append(ft.dropdown.Option(text = n.StateNme,
                                                                  data = n,
                                                                  on_click=self.readDD))
        self._view.update_page()

    def handleRaggiungibili(self,e):
        if self.ddCountry is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire stato di partenza"))
            return
        else:
            listaNodi = self._model.getRaggiungibiliTree(self.ddCountry)
            #listaNodi = self._model.getRaggiungibiliRecorsive2(self.ddCountry)
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Stati raggiunti: {len(listaNodi)}"))
            for n in listaNodi:
                self._view._txt_result.controls.append(ft.Text(n))
            self._view.update_page()


    def readDD(self, e):
        if e.control.data is None:
            self.ddCountry = None
        else:
            self.ddCountry = e.control.data


