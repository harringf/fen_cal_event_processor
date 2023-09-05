from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

ID_CALENDAR = "levi.costa1@gmail.com"

creds = service_account.Credentials.from_service_account_file(
    'cred.json', scopes=[
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events',
        'https://www.googleapis.com/auth/calendar.events.readonly',

    ])
calendar_service = build('calendar', 'v3', credentials=creds)

def events_calendar():
    # Data atual
    now = datetime.datetime.utcnow()

    # Data atual + 6 meses
    six_months_later = now + datetime.timedelta(days=180)

    time_min = now.isoformat() + 'Z'
    time_max = six_months_later.isoformat() + 'Z'

    events_result = calendar_service.events().list(
        calendarId=ID_CALENDAR,
        timeMin=time_min,
        timeMax=time_max,
        maxResults=10,  # Número máximo de eventos a serem retornados
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    return events_result.get('items', [])


for event in events_calendar():
    event_name = event['summary']
    event_start = event['start'].get('dateTime', event['start'].get('date'))
    event_description = event.get('description', 'Nenhuma descrição disponível.')
    event_location = event.get('location', 'Nenhum endereço disponível.')

    print(f'Nome do Evento: {event_name}')
    print(f'Data e Hora do Evento: {event_start}')
    print(f'Endereço: {event_location}')
    print(f'Descrição do Evento: {event_description}')
    print('---')