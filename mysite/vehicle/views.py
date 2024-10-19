from django.shortcuts import render

vehicles = [
    {'id': 1, 'name': 'Toyota Corolla', 'model': '2020', 'license': 'ABC123', 'status': 'Available'},
    {'id': 2, 'name': 'Ford F-150', 'model': '2018', 'license': 'XYZ789', 'status': 'In Maintenance'},
    # Add more vehicles...
]

# Create your views here.
def vehicles_page(request):
    return render(request, 'vehicles.html')

def vehicle_detail_page(request, id):
    vehicle = next((v for v in vehicles if v['id'] == int(id)), None)

    if vehicle is None:
        return render(request, '404.html')
    
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})