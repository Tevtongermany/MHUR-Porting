using RestSharp;

namespace MHURPorting.Services.Endpoints;

public abstract class AbstractApiProvider
{
    protected RestClient _client;

    protected AbstractApiProvider(RestClient client)
    {
        _client = client;
    }
}