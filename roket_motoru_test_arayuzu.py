import flet as ft


def main(page: ft.Page):
    page.window_width = 900
    page.window_height = 650
    # page.title =
    page.bgcolor = "0xFF2E2E2E"
    page.window_frameless = True
    page.window_center()

    def ust_panel():
        return ft.Row(controls=[
            ft.Icon(color=ft.colors.WHITE60, size=25, name=ft.icons.ROCKET_LAUNCH_ROUNDED),
            ft.Text(
                value="GÜROK KY-1 ROKET MOTORU STATİK ATEŞLEME TEST DÜZENEĞİ ARAYÜZÜ",
                color=ft.colors.WHITE60,
            ),

            ft.Row(
                controls=[
                    # ekrani kapla (fonksiyon verilmeyecek!)
                    ft.IconButton(icon=ft.icons.CIRCLE,
                                  icon_color=ft.colors.ORANGE_700,
                                  offset=ft.Offset(1, 0), ),
                    # ekrani asagi indir (fonksiyon verilmeyecek!)
                    ft.IconButton(
                        icon=ft.icons.CIRCLE,
                        icon_color=ft.colors.GREEN_700,
                        offset=ft.Offset(0.5, 0),
                    ),
                    # uygulamayi sonlandir
                    ft.IconButton(
                        icon=ft.icons.CIRCLE,
                        icon_color=ft.colors.RED_700,
                        on_click=lambda e: page.window_close(),
                    ),

                ],
                offset=ft.Offset(1.6, 0),
            ),

        ],
            offset=ft.Offset(0, -0.2),
        )

    def grafikler():
        return ft.Row(controls=[
            # ---------------- ITKI GRAM GRAFIGI KODLARI
            ft.Stack(controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[

                        ],
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["0xFF414040", "0xFF404040"],
                    ),

                    width=320,
                    height=240,
                    padding=10,
                    border_radius=10,

                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="İtki grafiği (gr)",
                                size=16,
                                offset=ft.Offset(0, 0.2),
                                color=ft.colors.WHITE60,
                            ),
                        ],
                    ),
                    bgcolor="0xFF363636",
                    width=316,
                    height=236,
                    padding=10,
                    border_radius=10,
                    offset=ft.Offset(0.0075, 0.0075),

                ),
            ],
            ),

            # ---------------- ITKI NEWTON GRAFIGI KODLARI
            ft.Stack(controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[

                        ],
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["0xFF414040", "0xFF404040"],
                    ),

                    width=320,
                    height=240,
                    padding=10,
                    border_radius=10,

                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="İtki grafiği (N)",
                                size=16,
                                offset=ft.Offset(0, 0.2),
                                color=ft.colors.WHITE60,
                            ),
                        ],
                    ),
                    bgcolor="0xFF363636",
                    width=316,
                    height=236,
                    padding=10,
                    border_radius=10,
                    offset=ft.Offset(0.0075, 0.0075),

                ),
            ],
                offset=ft.Offset(0.2, 0),
            ),

        ],
            offset=ft.Offset(0.098, 0.05),
        )

    def veriler():
        return ft.Row(controls=[
            # ---------------- ITKI GRAM VERILERI KOD BLOGU
            ft.Stack(controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[

                        ],
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["0xFF414040", "0xFF404040"],
                    ),

                    width=320,
                    height=240,
                    padding=10,
                    border_radius=10,

                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # motor durumu gram
                            ft.Row(controls=[
                                ft.Text(
                                    value="Motor durumu",
                                    size=23,
                                    offset=ft.Offset(0.02, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[

                                        ],
                                    ),
                                    bgcolor=ft.colors.RED_700,
                                    width=23,
                                    height=23,
                                    border_radius=100,

                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER, ),
                            # anlik itki gram
                            ft.Row(controls=[
                                ft.Text(
                                    value="Anlık itki:",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Text(
                                    value="0 gram",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color="0xFFFFFFFF",
                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            # max itki gram
                            ft.Row(controls=[
                                ft.Text(
                                    value="Max itki:",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Text(
                                    value=" 0 gram",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color="0xFFFFFFFF",
                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER, ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER

                    ),
                    bgcolor="0xFF363636",
                    width=316,
                    height=236,
                    padding=10,
                    border_radius=10,
                    offset=ft.Offset(0.0075, 0.0075),

                ),
            ],
            ),

            # ---------------- ITKI NEWTON VERILERI KOD BLOGU
            ft.Stack(controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[

                        ],
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["0xFF414040", "0xFF404040"],
                    ),

                    width=320,
                    height=240,
                    padding=10,
                    border_radius=10,

                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # motor durumu newton
                            ft.Row(controls=[
                                ft.Text(
                                    value="Motor durumu",
                                    size=23,
                                    offset=ft.Offset(-0.06, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[

                                        ],
                                    ),

                                    bgcolor=ft.colors.RED_700,
                                    width=23,
                                    height=23,
                                    border_radius=100,
                                    offset=ft.Offset(-0.6, 0),

                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER, ),
                            # anlik itki newton
                            ft.Row(controls=[
                                ft.Text(
                                    value="Anlık itki:",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Text(
                                    value="0 newton",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color="0xFFFFFFFF",
                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            # max itki newton
                            ft.Row(controls=[
                                ft.Text(
                                    value="Max itki:",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color=ft.colors.WHITE60,
                                ),
                                ft.Text(
                                    value=" 0 newton",
                                    size=23,
                                    offset=ft.Offset(0, 0),
                                    color="0xFFFFFFFF",
                                ),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER, ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    bgcolor="0xFF363636",
                    width=316,
                    height=236,
                    padding=10,
                    border_radius=10,
                    offset=ft.Offset(0.0075, 0.0075),

                ),
            ],
                offset=ft.Offset(0.2, 0),
            ),

        ],
            offset=ft.Offset(0.098, 0.1),
        )

    def copyright_text():
        return ft.Row(controls=[
            ft.Text(
                value="Copyright 2023",
                size=16,
                offset=ft.Offset(0, 0),
                color="0xFFFFFFFF",
            ),
            ft.Text(
                value="©",
                size=16,
                offset=ft.Offset(-0.5, 0),
                color="0xFFF15509",
            ),
            ft.Text(
                value="rocketsoft.com.tr",
                size=16,
                offset=ft.Offset(-0.12, 0),
                color="0xFFA2A2A2",
            ),
            ft.Text(
                value="Alikper İslam",
                size=16,
                offset=ft.Offset(-0.22, 0),
                color="0xFFFFFFFF",
            ),
        ],
            offset=ft.Offset(0.3, 2.3),
        )

    # ------------------------------------ UI kodlari ---------------------------------
    ui = ft.Column(
        controls=[
            # UST PANEL BILGILER KISMI
            ust_panel(),
            # sol grafik
            grafikler(),
            # verilerin gosterimi
            veriler(),
            # copyright
            copyright_text(),

        ],
        height=page.height,
    )
    # ------------------------------------ UI kodlari ---------------------------------

    page.controls.append(ui)
    page.update()


ft.app(target=main)
