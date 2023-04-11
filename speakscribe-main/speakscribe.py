# This code is licensed under the terms of the GNU Lesser General Public License v2.1

from nicegui import ui

from components import audio_transcriber
from components import chat

ui_state = chat.UIState()
au_state = audio_transcriber.AUDIO_State()

@ui.page('/')
async def index_page() -> None:
    # Chat component is in components/chat.py
    await chat.content(ui_state)
    await audio_transcriber.content(au_state)

    # Footer
    with ui.footer().classes("font-mono bg-zinc-900"):
        ui.label(
            'This website was built using OpenAI and NiceGUI For DCC Lab By Bikash Singh Under Dr. Ghanshyam S. Bopche and Mr. Purushottam Kumar')


ui.run(dark=True, title='TBD')
